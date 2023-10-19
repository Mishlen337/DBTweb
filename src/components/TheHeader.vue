<template>
    <header>
        <b-navbar toggleable="lg" type="dark" variant="info">
            <b-navbar-brand to="/">
                <img src="../assets/logo.png" width="70px" >
            </b-navbar-brand>

            <b-navbar-toggle target="nav-collapse"></b-navbar-toggle>

            <b-collapse id="nav-collapse" is-nav>
                <b-navbar-nav>
                    <b-nav-item to="/about">О нас</b-nav-item>
                    <b-nav-item to="/employees">Специалисты</b-nav-item>
                    <b-nav-item href="#" disabled>Подбор</b-nav-item>
                    <b-nav-item href="#" disabled>Блог</b-nav-item>
                </b-navbar-nav>

                <b-navbar-nav class="ml-auto">
                    <b-nav-item-dropdown right>
                        
                        <template #button-content>
                            <em>Личный кабинет</em>
                        </template>
                        <b-dropdown-item href="https://n269840.yclients.com/profile?o=">Войти</b-dropdown-item>
                        <b-dropdown-item href="https://n269840.yclients.com/profile/records?o=">Мои записи</b-dropdown-item>
                    </b-nav-item-dropdown>
                </b-navbar-nav>
            </b-collapse>
        </b-navbar>
        <router-view/>
    </header>
</template>

<script>
export default {
    name: 'TheHeader'
}
</script>
