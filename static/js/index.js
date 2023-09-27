window.addEventListener("load", () => {
  const loaderBg = document.querySelector(".lds-facebook")
  let currentYearElement = document.querySelector('#current-year')

  if (currentYearElement) {
    currentYearElement.innerHTML = new Date().getFullYear()
  }
  if (loaderBg) {
    loaderBg.classList.add("disppear")
  }

  
})

