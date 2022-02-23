
if (window.history.replaceState){
 
    window.history.replaceState(null, null , window.location.href);
}


// console.log("this is working");
// var x = "hello";
// // alert(x); 

// x = 67;
// // alert(x);

// let y = 98;

// let = 89;

// alert(y); 
// // let does not allow to change value of variable

// // let is mostly used in functions, switch etc

// // loop

// var z = 0;

// for (z = 0; z<= 5 ; z++){

//     console.log(z)
// }


// validating button that it should not be empty

// search login button

// function validateform(){
//     x = document.forms["myform"]["fname"].value;
//     if (x == ""){
//         alert("Please Enter your name ...")

//     }
// }


//chnaging color on blank submit
// function validateform(){
//     x = document.forms["myform"]["fname"].value;
//     if (x == ""){
//         document.getElementById('fname').placeholder = "please enter name abc";
//         // to highlight border
//         document.getElementById('fname').style.border = "10px solid red";


// to show message above username

// first add div in base.html above username
//         var x = document.getElementById("valid");
//         x.innerHTML = "enter your email ";

//         x.style.color = "red";
//         x.style.border = "5px solid #f003fc";
//         return false;
        
//     }
// }



// first create div on page

// {/* 
//     <div id = "mydiv">
//     <div class = "myname1" id = "myname">abc 1</div>
//     <div type = "text" class = "myname1" id = "myname">abc 1</div>
//     <div type = "text" class = "myname1" id = "myname">abc 1</div>
    

// </div>

// //  */}


/* <button onclick="crelement()" >button</button> */

function crelement(){
    //element creation at top always
    x = document.getElementsByClassName("myname");
    console.log(x);
    x[0].innerHTML = "heyyyyyyyyy";

    x = document.createElement("input");
    z = document.createElement("label");
    x.setAttribute("class", "myname");


    y = document.getElementById("mydiv");

    //element append at last always


    y.appendChild(x);
    y.appendChild(z);

}



  









