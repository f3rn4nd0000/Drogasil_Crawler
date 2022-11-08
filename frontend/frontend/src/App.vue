<script>
import axios from "axios";

export default {
  data() {
    return {
      products: "",
      sucess: "",
      activeClass: "active"
    };
  },
  methods: {
    submitForm() {
      axios
        .post("http://127.0.0.1:8000/", {
          consulta: this.query,
        })
        .then((response) => {
          console.log('------------')
          console.log(response.data);
          this.response = response.data;
          this.sucess = 'Dados recuperados com sucesso';
        })
        this.products = "";
    },
  },
};
</script>

<template>
    <div class="searchbar" id="app">
    
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
        
        <div v-if="sucess">
          {{ sucess }}
          <div
            v-for="item in response.products"
            :key="item"
            class="my-card"
            style="width: 28rem"
          >
            <div v-if=" item.name ">
              <p>{{ item.name }}</p>
              <img :src="item.image" width="200" height="200">
              <h3> PREÇO: R${{ item.valueFrom }}</h3>
            </div>
          </div>

        </div>
      </form>

    </div>

</template>

<style scoped>

h1 {
  font-weight: 500;
  font-size: 1.8rem;
  top: -10px;
}

img{
  border-radius: 20px;
}

#my-button{
  margin-top:20px;
}

.my-card {
  /* Add shadows to create the "card" effect */
  box-shadow: 0 4px 8px 0 rgba(0,0,0,0.2);
  transition: 0.3s;
  border-radius: 20px; /* 5px rounded corners */
  margin:20px;
  text-align: left;
}

/* On mouse-over, add a deeper shadow */
.my-card:hover {
  box-shadow: 0 8px 16px 0 rgba(0,0,0,0.2);
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