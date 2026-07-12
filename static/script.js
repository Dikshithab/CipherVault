// ==========================
// ENCRYPT FILE NAME & INFO
// ==========================

const encryptFile = document.getElementById("encryptFile");

if (encryptFile) {

    encryptFile.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) return;

        document.getElementById("encryptFileName").innerText = file.name;

        document.getElementById("fileInfo").style.display = "block";

        document.getElementById("infoName").innerText = file.name;

        document.getElementById("infoSize").innerText =
            (file.size / 1024).toFixed(2) + " KB";

        document.getElementById("infoType").innerText =
            file.type || "Unknown";

    });

}

// ==========================
// DECRYPT FILE NAME
// ==========================

const decryptFile = document.getElementById("decryptFile");

if (decryptFile) {

    decryptFile.addEventListener("change", function () {

        const file = this.files[0];

        if (!file) return;

        document.getElementById("decryptFileName").innerText = file.name;

    });

}

// ==========================
// PASSWORD STRENGTH
// ==========================

const password = document.getElementById("password");

if (password) {

    password.addEventListener("input", function () {

        const value = password.value;

        let score = 0;

        if (value.length >= 8) score++;
        if (/[A-Z]/.test(value)) score++;
        if (/[a-z]/.test(value)) score++;
        if (/[0-9]/.test(value)) score++;
        if (/[^A-Za-z0-9]/.test(value)) score++;

        const bar = document.getElementById("strengthBar");
        const text = document.getElementById("strengthText");

        switch (score) {

            case 0:
            case 1:
                bar.style.width = "20%";
                bar.className = "progress-bar bg-danger";
                text.innerText = "Weak";
                break;

            case 2:
                bar.style.width = "40%";
                bar.className = "progress-bar bg-warning";
                text.innerText = "Fair";
                break;

            case 3:
                bar.style.width = "60%";
                bar.className = "progress-bar bg-info";
                text.innerText = "Good";
                break;

            case 4:
                bar.style.width = "80%";
                bar.className = "progress-bar bg-primary";
                text.innerText = "Strong";
                break;

            case 5:
                bar.style.width = "100%";
                bar.className = "progress-bar bg-success";
                text.innerText = "Very Strong";
                break;
        }

    });

}

// ==========================
// LOADER
// ==========================

document.querySelectorAll("form").forEach(function (form) {

    form.addEventListener("submit", function () {

        document.getElementById("loader").style.display = "flex";

    });

});

// ==========================
// DARK MODE
// ==========================

const themeBtn = document.getElementById("themeBtn");

function toggleTheme(isDark){

    document.body.classList.toggle("bg-dark", isDark);
    document.body.classList.toggle("text-light", isDark);

    document.querySelectorAll(".card, .feature-card, .algorithm-card, .file-info")
        .forEach(card=>{
            card.classList.toggle("bg-dark", isDark);
            card.classList.toggle("text-light", isDark);
        });

    if(isDark){
        themeBtn.innerHTML="☀️ Light Mode";
        localStorage.setItem("theme","dark");
    }else{
        themeBtn.innerHTML="🌙 Dark Mode";
        localStorage.setItem("theme","light");
    }
}

toggleTheme(localStorage.getItem("theme")==="dark");

themeBtn.addEventListener("click",function(){

    toggleTheme(!document.body.classList.contains("bg-dark"));

});