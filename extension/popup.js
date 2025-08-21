// popup.js

document.getElementById("summarize-button").addEventListener("click", function () {
    chrome.tabs.query({ active: true, currentWindow: true }, function (tabs) {
        const url = tabs[0].url;  // Get the URL of the active YouTube tab

        fetch(`http://127.0.0.1:5000/summarize?url=${encodeURIComponent(url)}`)
            .then(response => response.json())
            .then(data => {
                const summaryDiv = document.getElementById("summary");
                if (data.summary) {
                    summaryDiv.innerHTML = data.summary;  // Insert the summary text
                } else {
                    summaryDiv.innerHTML = "Error generating summary.";
                }
            })
            .catch(error => {
                const summaryDiv = document.getElementById("summary");
                summaryDiv.innerHTML = "Error generating summary: " + error;
            });
    });
});
