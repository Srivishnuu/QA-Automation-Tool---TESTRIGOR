let latestTestResult = null;

async function executeTest() {
  const url = document.getElementById("url").value;
  const stepsText = document.getElementById("steps").value;
  const testName = document.getElementById("testName").value;

  if (!url || !stepsText || !testName) {
    alert("Please fill all fields");
    return;
  }

  const steps = stepsText.split("\n").filter(s => s.trim() !== "");

  try {
    // SHOW LOADER
    document.getElementById("loader").style.display = "block";
    document.getElementById("results").innerHTML = "";
    document.getElementById("downloadBtn").style.display = "none";

    const res = await fetch("http://127.0.0.1:5000/run", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({
        url: url,
        steps: steps,
        testName: testName
      })
    });

    const data = await res.json();
    latestTestResult = data;

    renderResults(data);

  } catch (err) {
    document.getElementById("results").innerHTML =
      "<span style='color:red'>Backend connection failed</span>";
    console.error(err);
  } finally {
    // HIDE LOADER
    document.getElementById("loader").style.display = "none";
  }
}

function renderResults(data) {
  const container = document.getElementById("results");

  container.innerHTML = `
    <h3>${data.testName}</h3>
    <p><b>Run ID:</b> ${data.runId}</p>
    <h4 class="${data.status === "PASSED" ? "status-passed" : "status-failed"}">
      Status: ${data.status}
    </h4>
  `;

  data.steps.forEach(step => {
    const imgUrl = `http://127.0.0.1:5000/${step.screenshot}?t=${Date.now()}`;

    container.innerHTML += `
      <div class="step ${step.status === "FAILED" ? "failed" : ""}">
        <b>Step ${step.stepNumber}</b><br/>
        ${step.description}<br/>
        <span class="${step.status === "PASSED" ? "status-passed" : "status-failed"}">
          Status: ${step.status}
        </span><br/>
        ${step.error ? "Error: " + step.error : ""}
        <br/>
        <img src="${imgUrl}" width="500"/>
      </div>
    `;
  });

  document.getElementById("downloadBtn").style.display = "block";
}

function downloadReport() {
  if (!latestTestResult) {
    alert("No test results to download");
    return;
  }

  let html = `
    <html>
    <head>
      <title>QA Test Report</title>
      <style>
        body { font-family: Arial; padding: 20px; }
        .passed { color: green; }
        .failed { color: red; }
        .step { margin-bottom: 20px; border-bottom: 1px solid #ccc; }
      </style>
    </head>
    <body>
      <h2>${latestTestResult.testName}</h2>
      <p><b>Run ID:</b> ${latestTestResult.runId}</p>
      <p><b>Status:</b> ${latestTestResult.status}</p>
      <hr/>
  `;

  latestTestResult.steps.forEach(step => {
    html += `
      <div class="step">
        <h4>Step ${step.stepNumber}</h4>
        <p>${step.description}</p>
        <p class="${step.status === "PASSED" ? "passed" : "failed"}">
          ${step.status}
        </p>
        ${step.error ? `<p>Error: ${step.error}</p>` : ""}
      </div>
    `;
  });

  html += "</body></html>";

  const blob = new Blob([html], { type: "text/html" });
  const a = document.createElement("a");
  a.href = URL.createObjectURL(blob);
  a.download = "QA_Test_Report.html";
  a.click();
}
