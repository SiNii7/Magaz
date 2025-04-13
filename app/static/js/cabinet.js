
function f1(id, zakaz){
    console.log(id)
    elem = document.getElementById(id)
    if (elem.innerHTML){
        elem.innerHTML = ''
    }
    else {
        elem.innerHTML = 'Товары: <br>'+zakaz
    }
}