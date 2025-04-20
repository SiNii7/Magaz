let likes = document.getElementsByClassName('like')

for (l of likes){
    l.onclick = f1
}

function f1(event){
    console.log(event)
    console.log(event.target.id)
    let color
    if (event.target.src.includes('nolike')){
        event.target.setAttribute('src','/static/img/like.jpg')
        color='red'
    }
    else {
        event.target.setAttribute('src', '/static/img/nolike.jpg')
        color='white'
    }
    let url='tolike/'
        $.ajax(url,{
            method:'GET',
            data:{k1:event.target.id, k2:color},
            success: function (response){
                console.log(response.message)
            },
            error:function (response){
                console.log('ошибка')
                console.log(response)
            }
        })

}