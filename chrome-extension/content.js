async function rewriteText(text, lang) {
  // Replace this endpoint with your actual LLM server.
  const response = await fetch('https://example.com/rewrite', {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({text: text, language: lang})
  });
  const data = await response.json();
  return data.rewritten || text;
}

async function processPage(lang) {
  const walker = document.createTreeWalker(document.body, NodeFilter.SHOW_TEXT);
  const tasks = [];
  const nodes = [];
  let node;
  while ((node = walker.nextNode())) {
    const value = node.nodeValue.trim();
    if (value) {
      nodes.push(node);
      tasks.push(rewriteText(value, lang));
    }
  }
  const results = await Promise.all(tasks);
  results.forEach((newText, idx) => {
    nodes[idx].nodeValue = newText;
  });
}

chrome.runtime.onMessage.addListener((msg, sender, sendResponse) => {
  if (msg.action === 'simplify') {
    processPage(msg.lang);
  }
});
