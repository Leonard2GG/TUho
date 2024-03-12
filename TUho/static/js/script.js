const sidebar = document.querySelector(".sidebar");
const toggleBtn = document.querySelector(".toggle-btn");

toggleBtn.addEventListener("click", () =>{
    sidebar.classList.toggle("active");
})

const menuItemList = document.querySelectorAll('.list-item')

menuItemList.forEach(e => {
    e.addEventListener('click', () => {
        let currentlyActive = document.querySelector(".list-item.active")
        currentlyActive.classList.toggle("active")
        e.classList.toggle("active")
    })
})