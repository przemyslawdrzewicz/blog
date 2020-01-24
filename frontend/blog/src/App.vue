<template>
  <v-app>
    <v-row justify="center mb-3">
      <v-app-bar
      flat
      max-width="79%"
      style="border-radius: 3px;"
      >
        <v-btn class="mr-3" @click.stop="edit = !edit" v-if="isLogged">Edytuj</v-btn>
        <v-btn class="mr-3" v-if="edit" @click="dialog_url = !dialog_url">Zmień zdjęcie</v-btn>
        <v-btn v-if="edit" @click="(addCard = !addCard) && assignTemp(-1)">Dodaj artykuł</v-btn>
        <v-spacer></v-spacer>
        <v-btn v-if="!isLogged" @click.stop="dialog = true">Zaloguj</v-btn>
        <v-btn v-if="isLogged" @click="logout()">Wyloguj</v-btn>
          </v-app-bar>
    </v-row>
    <v-row justify="center">
    <v-img
      :src="url"
      max-width="79%"
      max-height="70vh"
      style="border-radius: 5px;"
    ></v-img>
  </v-row>
  <v-dialog
    v-model="dialog"
    max-width="290"
  >
    <v-card>
      <v-card-title>
        <span class="headline">Zaloguj się</span>
      </v-card-title>
      <v-card-text>
        <v-container>
          <v-form
            ref="form"
            v-model="valid"
          >
            <v-row no-gutters>
              <v-col cols="12">
                <v-text-field
                  v-model="userName"
                  label="Nazwa użytkownika"
                  required
                  :rules="nameRules"
                ></v-text-field>
              </v-col>
              <v-col cols="12">
                <v-text-field
                  v-model="userPassword"
                  label="Hasło"
                  type="password"
                  :rules="passRules"
                  required
                ></v-text-field>
              </v-col>
              <v-col cols="12" class="text-center">
                <!-- eslint-disable-next-line max-len -->
                <v-btn :disabled="!valid" color="blue darken-1" @click="login()">Zaloguj</v-btn>
              </v-col>
              <v-col v-if="errorLogin" cols="12" class="text-center mt-5">
                <p style="color: red;">Błędny login lub hasło</p>
              </v-col>
            </v-row>
          </v-form>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
  <v-dialog
    v-model="dialog_url"
    max-width="290"
  >
    <v-card>
      <v-card-title>
        <span class="headline">Zmień zdjęcie</span>
      </v-card-title>
      <v-card-text>
        <v-container>
            <v-row no-gutters>
              <v-col cols="12">
                <v-text-field
                  v-model="url"
                  label="Podaj url obrazka"
                ></v-text-field>
              </v-col>
              <v-col cols="12" class="text-center">
                <!-- eslint-disable-next-line max-len -->
                <v-btn color="blue darken-1" @click="change_url()">Zmień zdjęcie</v-btn>
              </v-col>
              <v-col v-if="errorLogin" cols="12" class="text-center mt-5">
                <p style="color: red;">Błędny url</p>
              </v-col>
            </v-row>
        </v-container>
      </v-card-text>
    </v-card>
  </v-dialog>
     <v-card
    class="mx-auto mt-5 mb-5 add-card"
    width="80%"
    v-if="addCard"
    outlined
  >
    <v-card-text>
      <div class="text-right">
      <v-btn icon @click="add_article()">
        <!-- eslint-disable-next-line max-len -->
        <v-icon color="green">note_add</v-icon>
      </v-btn>
      <v-btn icon>
        <!-- eslint-disable-next-line max-len -->
        <v-icon color="red" @click="addCard = !addCard">cancel</v-icon>
      </v-btn>
      </div>
      <!-- eslint-disable-next-line max-len -->
      <p class="display-1 text--primary text-center flex-container">
        <input class="text-center add-card" v-model="tempTitle"/>
      </p>
      <div class="text--primary">
        <v-textarea class="add-card text-area ma-10" solo flat no-resize v-model="tempContent"/>
      </div>
    </v-card-text>
  </v-card>
   <v-card
    class="mx-auto mt-5 mb-5"
    width="80%"
    v-for="(articleObj, index) in articleObject"
    :key="articleObj.fields.article_id"
  >
    <v-card-text>
      <div class="text-right">
      <v-btn icon v-if="edit && (articleObj.fields.edit == false)">
        <!-- eslint-disable-next-line max-len -->
        <v-icon color="green" @click="(articleObj.fields.edit = !articleObj.fields.edit) && assignTemp(index)">edit</v-icon>
      </v-btn>
      <div v-if="articleObj.fields.edit">
      <v-btn @click="save(articleObj.fields.article_id)" icon>
        <v-icon color="green">save</v-icon>
      </v-btn>
      <!-- eslint-disable-next-line max-len -->
      <v-btn icon v-if="articleObj.fields.edit" @click="delete_article(articleObj.fields.article_id)">
        <!-- eslint-disable-next-line max-len -->
        <v-icon color="green">delete</v-icon>
      </v-btn>
      <v-btn icon>
        <!-- eslint-disable-next-line max-len -->
        <v-icon color="red" @click="articleObj.fields.edit = !articleObj.fields.edit">cancel</v-icon>
      </v-btn>
      </div>
      </div>
      <p class="display-1 text--primary text-center mt-5">
        <span v-if="!articleObj.fields.edit">{{articleObj.fields.title}}</span>
        <!-- eslint-disable-next-line max-len -->
        <input class="text-center add-card" v-if="articleObj.fields.edit" v-model="tempTitle"/>
      </p>
      <div class="text--primary ml-10 mr-10 mt-8">
        <!-- eslint-disable-next-line max-len -->
        <v-textarea v-if="!articleObj.fields.edit" auto-grow readonly solo flat no-resize v-model="articleObj.fields.content"/>
        <!-- eslint-disable-next-line max-len -->
        <v-textarea class="add-card" v-if="articleObj.fields.edit" solo flat no-resize v-model="tempContent"/>
      </div>
    </v-card-text>
    <v-card-actions>
    </v-card-actions>
  </v-card>
  </v-app>
</template>

<script>
import axios from 'axios';

export default {
  name: 'App',
  data() {
    return {
      dialog: false,
      userName: '',
      userPassword: '',
      edit: false,
      nameRules: [
        v => !!v || 'Brak nazwy użytkownika',
        v => (v.length >= 5 && v.length <= 15) || 'Nazwa musi być krótsza od 16 znaków i dłuższa od 4 znaków',
      ],
      passRules: [
        v => !!v || 'Brak hasła użytkownika',
        v => (v.length >= 5 && v.length <= 15) || 'Nazwa musi być krótsza od 16 znaków i dłuższa od 4 znaków',
      ],
      valid: false,
      articleObject: {},
      tempArticleObject: {},
      tempTitle: '',
      tempContent: '',
      addCard: false,
      isLogged: false,
      errorLogin: false,
      url: 'https://www.kwestiasmaku.com/sites/v123.kwestiasmaku.com/files/pasztet_sojowy_01.jpg',
      dialog_url: false,
    };
  },
  methods: {
    login() {
      const data = {};
      data.username = this.userName;
      data.password = this.userPassword;

      axios.post('http://localhost:8000/auth/', data).then((res) => {
        console.log(res);
        this.$session.start();
        this.$session.set('token', res.data.token);
        this.dialog = false;
        this.errorLogin = false;
        this.init();
      }).catch(() => {
        this.errorLogin = true;
      });
    },
    init() {
      const dataText = {};
      axios.post('http://127.0.0.1:8000/polls/get_articles/', dataText).then((response) => {
        let obj = {};
        obj = JSON.parse(response.data);
        obj.forEach((value, i) => {
          obj[i].fields.edit = false;
        });
        this.articleObject = obj;
        this.tempArticleObject = obj;
        console.log(this.tempArticleObject);
        this.get_url();
      });

      this.$session.start();
      if (!this.$session.has('token')) {
        this.isLogged = false;
        console.log('wylogowany');
      } else {
        this.isLogged = true;
        console.log('zalogowany');
      }
    },
    assignTemp(index) {
      if (index !== -1) {
        this.tempTitle = this.articleObject[index].fields.title;
        this.tempContent = this.articleObject[index].fields.content;
      } else {
        this.tempTitle = 'Dodaj tytuł';
        this.tempContent = 'Dodaj treść';
      }
    },
    add_article() {
      const size = this.articleObject[0].fields.article_id;
      const dataText = {};
      dataText.title = this.tempTitle;
      dataText.content = this.tempContent;
      dataText.article_id = size + 1;

      axios.post('http://127.0.0.1:8000/polls/add_article/', dataText).then((response) => {
        this.init();
        console.log(response);
      });
      this.addCard = false;
    },
    save(key) {
      const data = {};
      data.title = this.tempTitle;
      data.content = this.tempContent;
      data.id = key;

      axios.post('http://127.0.0.1:8000/polls/update_article/', data).then((response) => {
        this.init();
        console.log(response);
      });
    },
    delete_article(key) {
      const data = {};
      data.id = key;

      axios.post('http://127.0.0.1:8000/polls/delete_article/', data).then((response) => {
        this.init();
        console.log(response);
      });
    },
    logout() {
      this.edit = false;
      this.addCard = false;
      this.$session.destroy();
      this.init();
    },
    change_url() {
      const data = {};
      data.url = this.url;

      axios.post('http://127.0.0.1:8000/polls/change_image/', data).then((response) => {
        this.get_url();
        console.log(response);
        this.dialog_url = false;
      });
    },
    get_url() {
      const dataText = {};
      axios.post('http://127.0.0.1:8000/polls/get_url/', dataText).then((response) => {
        let obj = {};
        obj = JSON.parse(response.data);
        this.url = obj[0].fields.url;
      });
    },
  },
  mounted() {
    this.init();
  },
};
</script>

<style scoped>
.add-card {

  border: 1px dotted  red !important;
  border-radius: 5px;
}

input:focus {
  outline: none;
}
p {
  border-bottom: 1px solid black;
padding-bottom: 5px;
}
</style>
