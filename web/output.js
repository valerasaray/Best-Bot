window.onload = function(){
    var text = document.getElementById("input");
    var button = document.getElementById("but");
    var list = document.querySelector(".chat");
    button.addEventListener("click",function(){
        if(text.value){
            addItem(text.value);
            text.value = "";
        }
    });

    async function chatBot(value){

        var item = document.createElement("li");
        var box = document.createElement("div");
        var me = document.createElement("div");

        me.classList.add("me");

        box.classList.add("l");
        box.innerHTML = await eel.f(value)();
        item.appendChild(me);
        item.appendChild(box);
        list.appendChild(item);

}



    function addItem(value){


        var item = document.createElement("li");
        var box = document.createElement("div");

        box.classList.add("r");
        box.innerHTML = value;
        item.appendChild(box);
        list.appendChild(item);
        chatBot(text.value);
    }
}

