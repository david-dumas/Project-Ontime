<template>
    <div class='header'>
        <router-link to="/" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Log uit
                </div>
        </router-link>

        <router-link to="/help" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Help
                </div>
        </router-link>
        
        <router-link to="/agenda" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Agenda
                </div>
        </router-link>
        
        <router-link to="/begeleider-dashboard" active-class="active" tag="button" exact class="nav-btn">
                <div class="link-container">
                    Dashboard
                </div>
        </router-link>
            
    </div>
</template>

<script>
export default {
    name: 'Header'
}
</script>
<style>
    .header{
        background-color: #22606D;
        overflow:hidden;
    }
    .header a{
        float:right;
        color: white;
        padding: 14px 16px;
        font-size: 17px;
        text-decoration: none;
        margin-right: 5%;
    }
    .header a:hover{
        background: #E5EFF3;
        color: #333;
    }

    .title{
    padding-top: 10%;
    font-size: 50px;
}

.navbar{
    height: 100vh;
    background-color: #578590;
}

.menu-items{
    padding-top: 10%;
}

.nav-btn{
    font-size: 30px;
    color: white;
    text-decoration: none;
}
</style>