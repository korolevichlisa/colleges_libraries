window.addEventListener("load", () => {
  const loaderBg = document.querySelector(".loader_bg")
  let currentYearElement = document.querySelector('#current-year')

  if (currentYearElement) {
    currentYearElement.innerHTML = new Date().getFullYear()
  }
  if (loaderBg) {
    loaderBg.classList.add("disppear")
  }

  
})

