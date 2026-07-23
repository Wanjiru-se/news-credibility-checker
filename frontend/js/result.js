const storedResult = localStorage.getItem("credibilityResult");

const credibilityScore = document.getElementById("credibilityScore");
const claimsContainer = document.getElementById("claimsContainer");

if (!storedResult) {
    credibilityScore.textContent = "No result";

    claimsContainer.innerHTML = `
        <div class="alert alert-warning">
            No credibility report was found. Please analyze an article first.
        </div>
    `;
} else {
    const result = JSON.parse(storedResult);

    credibilityScore.textContent = `${result.credibilityScore}%`;

    result.claims.forEach(function (claim) {
        const claimCard = document.createElement("div");

        claimCard.className = "card mb-3";

        claimCard.innerHTML = `
            <div class="card-body">

                <h5 class="card-title">
                    ${claim.claim}
                </h5>

                <p class="mb-2">
                    <strong>Status:</strong>
                    ${claim.status}
                </p>

                <a
                    href="${claim.source}"
                    target="_blank"
                    rel="noopener noreferrer">

                    View supporting source

                </a>

            </div>
        `;

        claimsContainer.appendChild(claimCard);
    });
}