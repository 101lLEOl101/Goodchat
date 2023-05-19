<template>
    <div class="messenger_box" id="messenger_box">
    <h2 style="text-align:center;"> Личные сообщения </h2>
    
    </div>
  </template>
  
  <script>
  export default {}
  </script>
  
  <style>
  .messenger_box{
    background-color: rgba(0,0,0,60%);
    width: 70%;
    height: 84vh;
    margin: 0 auto;
    color: white;
    padding-top: calc(7vh + 5px);
    border-bottom-left-radius: 12px;
    border-bottom-right-radius: 12px;
    box-shadow: 0px 0px 33px #8270F2;
    overflow-y: auto;
    overflow-x: hidden;
    font-size: smaller;
}

.messenger_box::-webkit-scrollbar {
  width: 10px;
}

.messenger_box::-webkit-scrollbar-track {
  background-color: rgba(0,0,0, 0);
  border-bottom-right-radius: 100px;
}

.messenger_box::-webkit-scrollbar-thumb {
  border-top-right-radius: 100px;
  border-top-left-radius: 100px;
  border-bottom-right-radius: 300px;
  background-color: rgba(130, 112, 242, 70%);
}
  </style>
  