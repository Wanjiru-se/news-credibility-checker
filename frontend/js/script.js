// Get the radio buttons
const textOption = document.getElementById("textOption");
const urlOption = document.getElementById("urlOption");

// Get the input sections
const textInputSection = document.getElementById("textInputSection");
const urlInputSection = document.getElementById("urlInputSection");

// When "Paste Article Text" is selected
textOption.addEventListener("change", function () {

    if (textOption.checked) {

        textInputSection.classList.remove("d-none");
        urlInputSection.classList.add("d-none");

    }

});

// When "Enter Article URL" is selected
urlOption.addEventListener("change", function () {

    if (urlOption.checked) {

        urlInputSection.classList.remove("d-none");
        textInputSection.classList.add("d-none");

    }

});

const analyzeButton = document.getElementById("analyzeButton");
const articleText = document.getElementById("articleText");
const articleUrl = document.getElementById("articleUrl");

analyzeButton.addEventListener("click", async function () {
    let inputType;
    let content;

    if (textOption.checked) {
        inputType = "text";
        content = articleText.value.trim();
    } else {
        inputType = "url";
        content = articleUrl.value.trim();
    }

    if (!content) {
        alert("Please provide article text or a news article URL.");
        return;
    }

    analyzeButton.disabled = true;
    analyzeButton.textContent = "Analyzing...";

    try {
        const response = await fetch("http://127.0.0.1:5000/analyze", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                inputType: inputType,
                content: content
            })
        });

        const result = await response.json();

        if (!response.ok) {
            alert(result.error || "Something went wrong.");
            return;
        }

        localStorage.setItem(
            "credibilityResult",
            JSON.stringify(result)
        );

        window.location.href = "result.html";

    } catch (error) {
        alert("Could not connect to the backend. Make sure Flask is running.");
        console.error(error);

    } finally {
        analyzeButton.disabled = false;
        analyzeButton.textContent = "Analyze Article";
    }
});