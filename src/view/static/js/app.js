document.addEventListener('DOMContentLoaded', () => {
    const analyzeBtn = document.getElementById('analyze-btn');
    const logInput = document.getElementById('log-input');
    const resultDiv = document.getElementById('result');
    const loadingDiv = document.getElementById('loading');

    analyzeBtn.addEventListener('click', async () => {
        const logs = logInput.value.trim();
        
        if (!logs) {
            alert('Please paste some logs first.');
            return;
        }

        resultDiv.textContent = '';
        loadingDiv.classList.remove('hidden');
        analyzeBtn.disabled = true;

        try {
            const response = await fetch('/api/analyze', {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                },
                body: JSON.stringify({ logs }),
            });

            const data = await response.json();

            if (response.ok) {
                resultDiv.textContent = data.analysis;
            } else {
                resultDiv.innerHTML = `<span class="error">Error: ${data.error}</span>`;
            }
        } catch (error) {
            resultDiv.innerHTML = `<span class="error">Connection error: ${error.message}</span>`;
        } finally {
            loadingDiv.classList.add('hidden');
            analyzeBtn.disabled = false;
        }
    });
});
