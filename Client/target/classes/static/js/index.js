
function getUserInfo() {
        let xhr = new XMLHttpRequest();
        xhr.open('GET', '/userInfo', true);
        xhr.onload = function () {
                document.getElementById('userInfo').innerText = this.responseText;
        };
        xhr.send();
}
window.onload = getUserInfo

