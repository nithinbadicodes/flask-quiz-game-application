console.log("JS loaded");


// ================= PLAY BUTTON =================
const playButton = document.getElementById("play-btn");

if (playButton) {
    playButton.addEventListener("click", () => {
        // window.location.href = "/quiz";
        window.location.href = "/start";
    });
}


// ================= POPUPS =================
const difficultyPopup = document.getElementById("difficulty-popup");
const instructionsPopup = document.getElementById("instructions-popup");
const hintPopup = document.getElementById("hint-popup")


const difficultyBtn = document.getElementById("difficulty-btn");
const instructionsBtn = document.getElementById("instructions-btn");
const hintBtn = document.getElementById("hint-btn")


const difficultyOptions = document.querySelectorAll(".difficulty-option");
const display = document.getElementById("difficulty-display");

// OPEN POPUPS
if (difficultyBtn) {
    difficultyBtn.addEventListener("click", () => {
        difficultyPopup.classList.add("active");
    });
}

if (instructionsBtn) {
    instructionsBtn.addEventListener("click", () => {
        instructionsPopup.classList.add("active");
    });
}

if (hintBtn) {
    hintBtn.addEventListener("click",()=>{
        hintPopup.classList.add("active")
    })
}

if (hintPopup){
    hintPopup.addEventListener("click",(e)=>{
        if (e.target == hintPopup){
            hintPopup.classList.remove("active")
        }
    })
}

// CLOSE POPUPS
[difficultyPopup, instructionsPopup].forEach(popup => {
    if (popup) {
        popup.addEventListener("click", (e) => {
            if (e.target === popup) {
                popup.classList.remove("active");
            }
        });
    }
});

// ================= DIFFICULTY =================
difficultyOptions.forEach(button => {
    button.addEventListener("click", () => {
        const level = button.textContent;

        if (display) {
            display.textContent = "Difficulty Level: " + level;
        }

        // send difficulty to Flask
        fetch("/set_difficulty", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ difficulty: level })
        });

        difficultyPopup.classList.remove("active");
    });
});

// ================= QUIZ =================
// const options = document.getElementsByClassName("options");
const options = document.querySelectorAll(".options");
const nextBtn = document.getElementById("next-btn");
const prevBtn = document.getElementById("prev-btn");

// OPTION CLICK → send answer to Flask
// [...options].forEach((option, index) => {
options.forEach((option, index) => {
    option.addEventListener("click", () => {

        fetch("/answer", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify({ answer: index })
        })
        .then(res => res.json())
        .then(data => {

            options.forEach(opt => {
                opt.style.backgroundColor = "";
            });

            // highlight selected
            option.style.backgroundColor = "lightblue";
        });
    });
});

// ================= NAVIGATION =================
if (nextBtn) {
    nextBtn.addEventListener("click", () => {
        window.location.href = "/next";
    });
}

if (prevBtn) {
    prevBtn.addEventListener("click", () => {
        window.location.href = "/prev";
    });
}

// ================= FINAL PAGE =================
const returnButton = document.getElementById("return-btn");

if (returnButton) {
    returnButton.addEventListener("click", () => {
        window.location.href = "/";
    });
}