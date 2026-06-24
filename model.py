ELEMENT_MAP = {
    
    # USER NAME
    "username": """
        input[name*='UserName'],
        input[placeholder*='Username'],
        input[name*='email']
    """,

    "first name": """
        input[name*='First Name'],
        input[placeholder*='First Name'],
        input[name*='FirstName']
    """,
    
    "last name": """
        input[name*='Last Name'],
        input[placeholder*='Last Name'],
        input[name*='LastName']
    """,

    # USER LOGIN AND EMAIL
    "user login": """
        input[name*='User Login'],
        input[placeholder*='User Login'],
        input[name*='email']
    """,

    "email": """
        input[placeholder*='Email'],
        input[name*='UserNameINR'],
        input[class*='regemail']
    """,

    # PASSWORD SECTION
    "new password": "input[id*='txtNewPassword']",
    
    "password": """
        input#Password,
        input[name$='$Password'],
        input[id='ctl00_placeholderMain_LoginView1_defaultLogin_Password'],
        input[type='password']:not([id*='Confirm'])
    """,
    
    # SPECIFIC FOR THE REGERASTRATION FIELD PASSWORD - MYR/USD PAGE
    "reg password": """
        input#Password.regspaswd
    """,

    "confirm password": """
        input[id*='ConfirmPassword'],
        input[placeholder*='Confirm Password']
    """,
    
    "search": "input[type='text']",

    "name": "input[placeholder*='Name'], input[name*='name']",

    
    # Register page mobile fallback
    "mobile number": "input[type='number'], input[placeholder*='Mobile']",
    "mobile": "input[type='number'], input[placeholder*='Mobile']",
    "phone": "input[type='number']",

    # ASP.NET register mobile field
    "number": "input[name*='txtMobile']",

    # OTP AND VERIFICATION
    "otp": "input[placeholder*='OTP'], input[name*='otp']",
    "verification code": "input[placeholder*='Verification Code'], input[name*='VerificationCode']",
    
    # SELECT COUNTRY IN THE REGISTER PAGE MYR/USD
    "country": "select#ddlCountry"
}



def parse_human_steps(steps, url):
    structured = []

    for raw in steps:
        raw = raw.strip()
        if not raw:
            continue

        step = raw.lower()

        if step.startswith("open"):
            structured.append({"action": "open", "raw": raw})

        elif step.startswith("type"):
            try:
                after = raw[5:].strip()
                parts = after.split(" in ")
                value = parts[0].strip()
                field = parts[1].strip().lower()
            except:
                value = ""
                field = "search"

            structured.append({
                "action": "type",
                "target": ELEMENT_MAP.get(field, "input"),
                "value": value,
                "raw": raw
            })

        elif step.startswith("click checkbox"):
            structured.append({
                "action": "click_checkbox",
                "target": raw[len("Click checkbox"):].strip(),
                "raw": raw
            })

        elif step.startswith("click button"):
            structured.append({
                "action": "click_button",
                "target": raw[len("Click button"):].strip(),
                "raw": raw
            })

        elif step.startswith("click link"):
            structured.append({
                "action": "click_link",
                "target": raw[len("Click link"):].strip(),
                "raw": raw
            })

        elif step.startswith("click input"):
            structured.append({
                "action": "click_input",
                "target": raw[len("Click input"):].strip(),
                "raw": raw
            })

        elif step.startswith("click"):
            structured.append({
                "action": "click",
                "target": raw[len("Click"):].strip(),
                "raw": raw
            })

        elif step.startswith("verify"):
            structured.append({
                "action": "verify",
                "target": raw[len("Verify"):].strip(),
                "raw": raw
            })

        elif step.startswith("wait until"):
            text = step.replace("wait until", "").strip()

            if "page is loaded" in text:
                structured.append({"action": "wait_for_page", "raw": raw})

        elif step.startswith("wait"):
            try:
                secs = int(step.replace("wait", "").strip())
            except:
                secs = 2

            structured.append({
                "action": "wait",
                "value": secs,
                "raw": raw
            })

        elif step.startswith("press"):
            structured.append({
                "action": "press",
                "value": raw[len("Press"):].strip(),
                "raw": raw
            })

        elif step.startswith("hover"):
            structured.append({
                "action": "hover",
                "target": raw.replace("Hover", "").strip(),
                "raw": raw
            })
            
        elif step.startswith("select"):
            try:
                after = raw[7:].strip()
                parts = after.split(" in ")
                value = parts[0].strip()
                field = parts[1].strip().lower()
            except:
                value = ""
                field = ""

            structured.append({
                "action": "select",
                "target": ELEMENT_MAP.get(field, "select"),
                "value": value,
                "raw": raw
            })


        else:
            raise ValueError(f"Unsupported step: {raw}")

    return structured