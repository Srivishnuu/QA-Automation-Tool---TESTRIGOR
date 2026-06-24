import uuid
import time
from pathlib import Path
from playwright.sync_api import sync_playwright

BASE_STORAGE = Path("backend/storage/runs")
BASE_STORAGE.mkdir(parents=True, exist_ok=True)


def handle_astroved_popup(page):
    try:
        page.get_by_text("NO", exact=False).click(timeout=1500)
    except:
        pass


def reliable_type(page, selector, value):
    field = page.locator(selector).first
    field.wait_for(state="visible", timeout=15000)
    field.scroll_into_view_if_needed()

    handle_astroved_popup(page)

    field.click()
    field.fill("")
    field.fill(value)

    if field.input_value() != value:
        field.fill(value)


def run_test(url, steps, test_name):
    results = []
    run_id = str(uuid.uuid4())[:8]

    run_dir = BASE_STORAGE / run_id
    run_dir.mkdir(parents=True, exist_ok=True)

    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context(permissions=[])
        page = context.new_page()

        page.set_default_timeout(60000)

        for i, step in enumerate(steps, start=1):
            screenshot_path = run_dir / f"step_{i}.png"

            try:
                action = step["action"]
                target = step.get("target")
                value = step.get("value")

                handle_astroved_popup(page)

                if action == "open":
                    page.goto(url)
                    page.wait_for_load_state("networkidle")

                elif action == "click":
                    locator = page.get_by_text(target, exact=False).first
                    locator.wait_for(state="visible")
                    locator.click()

                elif action == "click_button":
                    page.get_by_role("button", name=target).click()

                elif action == "click_link":
                    page.get_by_role("link", name=target).click()

                elif action == "click_input":
                    page.locator(f"input[value='{target}']").click()

                elif action == "click_checkbox":
                    checkbox = page.get_by_role("checkbox", name=target)
                    checkbox.wait_for(state="visible")
                    checkbox.check()

                elif action == "type":
                    reliable_type(page, target, value)

                elif action == "verify":
                    page.get_by_text(target, exact=False).first.wait_for()

                elif action == "wait":
                    time.sleep(value)

                elif action == "wait_for_page":
                    page.wait_for_load_state("networkidle")

                elif action == "wait_visible":
                    page.get_by_text(target, exact=False).first.wait_for(
                        state="visible"
                    )

                elif action == "wait_clickable":
                    locator = page.get_by_text(target, exact=False).first
                    locator.wait_for(state="visible")
                    locator.is_enabled()

                elif action == "wait_text":
                    page.get_by_text(target, exact=False).first.wait_for()

                elif action == "press":
                    page.keyboard.press(value)

                elif action == "hover":
                    locator = page.get_by_text(target, exact=False).first
                    locator.wait_for(state="visible")
                    locator.hover()
                    
                elif action == "select":
                    dropdown = page.locator(target).first
                    dropdown.wait_for(state="visible")
                    dropdown.select_option(label=value)


                page.screenshot(path=str(screenshot_path))

                results.append({
                    "stepNumber": i,
                    "description": step["raw"],
                    "status": "PASSED",
                    "screenshot": f"storage/runs/{run_id}/step_{i}.png"
                })

            except Exception as e:
                page.screenshot(path=str(screenshot_path))

                results.append({
                    "stepNumber": i,
                    "description": step["raw"],
                    "status": "FAILED",
                    "error": str(e),
                    "screenshot": f"storage/runs/{run_id}/step_{i}.png"
                })

        browser.close()

    return {
        "testName": test_name,
        "runId": run_id,
        "status": "PASSED" if all(r["status"] == "PASSED" for r in results) else "FAILED",
        "steps": results
    }