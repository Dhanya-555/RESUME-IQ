async function careerRoadmap() {

    let role =
        document.getElementById("role").value;

    let response = await fetch(
        "http://127.0.0.1:8000/career-roadmap",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                role: role
            })
        }
    );

    let data = await response.json();

    document.getElementById("result").innerHTML =
        JSON.stringify(data);
}
async function askBot() {

    const question =
    document.getElementById("question").value;

    const response = await fetch(
        "http://127.0.0.1:8000/career-chatbot",
        {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({
                question: question
            })
        }
    );

    const data = await response.json();

    document.getElementById("chatAnswer").innerHTML =
        data.answer;
}
fetch("http://127.0.0.1:8000/test")
.then(response => response.json())
.then(data => {
    alert(data.message);
})
.catch(error => {
    console.log("Connection failed:", error);
})
document.getElementById("resumeForm").addEventListener("submit", async (e) => {
    e.preventDefault();

    const data = {
        name: document.getElementById("name").value,
        email: document.getElementById("email").value,
        skills: document.getElementById("skills").value
    };

    const response = await fetch("http://127.0.0.1:8000/resume", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify(data)
    });

    const result = await response.json();
    alert(result.message);
});