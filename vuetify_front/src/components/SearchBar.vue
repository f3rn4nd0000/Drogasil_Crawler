<script>
import axios from "axios";
// import MyCard from './MyCard.vue';

export default {
    // components: { MyCard },
    data() {
        return {
            products: "",
            sucess: "",
            activeClass: "active",
            loading: false,
            response: "",
        };
    },
    methods: {
        submitForm() {
            this.loading = true
            axios
            .post("http://127.0.0.1:8000/", {
                consulta: this.query,
            })
            .then((response) => {
                console.log("------------");
                console.log(response.data);
                this.response = response.data;
                this.sucess = "Dados recuperados com sucesso";
                this.loading = false
            })
            this.products = "";
            },
        },
    };
</script>

<template>

    <div class="searchbar" id="app">
        <!-- <h1 style="margin-bottom: 200px; background-color:white; color:black;">DROGASIL CRAWLER</h1> -->
        <form @submit.prevent="submitForm">
            <div>
            <div class="label-test">
                <label for="query">Busca:</label><br />
                <input id="query" type="text" v-model="query" required />
            </div>

            <button
                :class="[consulta ? activeClass : '']"
                type="submit"
                id="my-button"
            >
                Pesquisar
            </button>
            </div>

            <div v-if="loading">
                <div class="text-center">
                    <v-progress-circular :size="150" :width="7" color="red" indeterminate></v-progress-circular>
                </div>
            </div>    
            <div v-if="sucess">
                <div
                    v-for="item in response.products"
                    :key="item"
                >
                    <div v-if="item.name">
                        {{ item.name }}
                        {{ item.image }}
                        <v-card :loading="loading" class="mx-auto my-12" max-width="374">
                        <v-img
                            height="200px"
                            width="400px"
                            :src="String(item.image).replace('//','https://')"
                            aspect-ratio="1"
                        ></v-img>
                        <v-card-title>{{ item.name }}</v-card-title>
                        <v-card-text>
                            <div class="my-4 text-subtitle-1">{{ item.qty }}</div>
                            <div class="my-4 text-subtitle-1">{{ item.brand }}</div>
                        </v-card-text>
                        <v-divider class="mx-4"></v-divider>
                            <v-card-actions>
                                <v-btn color="purple" text>
                                    <a :href="urlKey" />
                                </v-btn>
                            </v-card-actions>
                        </v-card>

                    </div>
                </div>
            </div>
        
        </form>
    </div>
</template>

<style scoped>

.v-progress-circular {
    margin: 10rem;
}

h1 {
    font-weight: 500;
    font-size: 1.8rem;
    top: -10px;
}

.img {
    border-radius: 20px;
}

#my-button {
    margin-top: 20px;
}

.my-card {
  /* Add shadows to create the "card" effect */
    box-shadow: 0 4px 8px 0 rgba(0, 0, 0, 0.2);
    transition: 0.3s;
    border-radius: 20px; /* 5px rounded corners */
    margin: 20px;
    text-align: left;
}

/* On mouse-over, add a deeper shadow */
.my-card:hover {
    box-shadow: 0 8px 16px 0 rgba(0, 0, 0, 0.2);
}

/* Add some padding inside the card container */
.container {
    padding: 2px 16px;
}

.searchbar {
    background-color: #2a2e32;
    color: white;
    font-size: 1rem;
    font-family: monospace;
    text-align: center;
    min-width: 32rem;
    height: 100%;
    width: 100%;
  /* position: absolute; */
}

h3 {
    font-size: 1.2rem;
}
.greetings h1,
.greetings h3 {
    text-align: center;
}

@media (min-width: 1024px) {
    .greetings h1,
    .greetings h3 {
        text-align: left;
    }
}
</style>



// old card 
// <p>{{ item.name }}</p>
//                         <v-container>
//                         <v-row
//                             align="rigth"
//                             align-content="rigth"
//                             class="text-rigth"
//                             >
//                             <v-col class="text-rigth">
//                                 <v-img class="img"
//                                     :src="item.image" 
//                                     width="200" 
//                                     height="200"></v-img>
//                                 <h3>PREÇO: R${{ item.valueFrom }}</h3>
//                             </v-col>
//                         </v-row>
//                         </v-container>
// class="my-card"
//                     style="width: 28rem"