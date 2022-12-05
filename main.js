const themeToggler = document.querySelector(".theme-toggler")

// change theme
themeToggler.addEventListener('click', () => {

     var SetTheme = document.body;
     SetTheme.classList.toggle('dark-theme-variables');

     var theme;
     if (SetTheme.classList.contains('dark-theme-variables')) {
          console.log('Dark mode');
          theme = "DARK";
     } else {
          console.log('Light mode');
          theme = "LIGHT";
     }
     localStorage.setItem("PageTheme", JSON.stringify(theme));

     themeToggler.querySelector('span:nth-child(1)').classList.toggle('active');
     themeToggler.querySelector('span:nth-child(2)').classList.toggle('active');
})

let GetTheme = JSON.parse(localStorage.getItem("PageTheme"));
console.log(GetTheme);

if (GetTheme === "DARK") {
     document.body.classList = 'dark-theme-variables';
}