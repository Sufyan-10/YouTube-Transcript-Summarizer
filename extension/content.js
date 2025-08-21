const videoUrl = window.location.href;  // Get the current YouTube video URL

chrome.runtime.sendMessage({ action: "getSummary", videoUrl: videoUrl }, (response) => {
  alert("Summary: " + response.summary);  // Show the summary in an alert (or you can customize this)
});
