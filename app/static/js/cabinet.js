
function f2(id, zakaz){
    console.log(id)
    elem = document.getElementById(id)
    if (elem.innerHTML){
        elem.innerHTML = ''
    }
    else {
        elem.innerHTML = 'Товары :'+zakaz
    }
}