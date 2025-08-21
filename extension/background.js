// background.js

chrome.runtime.onMessage.addListener(async (message, sender, sendResponse) => {
  if (message.action === "getSummary") {
    const videoUrl = message.videoUrl;
    try {
      const response = await fetch(`http://127.0.0.1:5000/summarize?url=${encodeURIComponent(videoUrl)}`);
      const summaryData = await response.json(); // Parse response as JSON
      console.log("Received summary data:", summaryData);  // Log for debugging
      sendResponse({ summary: summaryData.summary || "Summary could not be generated." });
    } catch (error) {
      console.error("Failed to fetch summary:", error);
      sendResponse({ summary: "Error fetching summary." });
    }
  }
  return true;  // Important to keep the message port open for async response
});
