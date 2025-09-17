const launchButton = document.getElementById("launchButton");

launchButton.addEventListener("click", function () {
    setTimeout(() => {
        launchButton.textContent = "3"

        setTimeout(() => {
            launchButton.textContent = "2"

            setTimeout(() => {
                launchButton.textContent = "1"
            
                setTimeout(() => {
                    launchButton.textContent = "Підтверджено: запуск ракети!";
                    launchButton.style.backgroundColor = "#e74c3c";
                    launchButton.style.color = "#ffffff";
                    launchButton.style.border = "2px solid #c0392b";
                    
                }, 1000)

            }, 1000)   

        }, 1000)

    }, 1000)
    
    

    });