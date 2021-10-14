<template>
    <footer class='footer'>
        <h1>OnTime</h1>
        <p1>© Copyrighted since 2021, all rights reserved</p1>
    </footer>

</template>

<script>
export default {
    name: 'Footer'
}
</script>

<style>
    .footer{
        bottom: 0;
        background-color: #153C44;
        color: white;
        overflow:hidden;
        position: fixed;
        left: 0;
        width: 100%;
        text-align: center;
    }
    .text {
        text-align: center;
    }
    h1{
        font-size: 30px;
        margin-right: 5%;
    }
    p {
        font-size: 10px;
        margin-right: 3%;
        padding-bottom: 20px;
    }
</style>