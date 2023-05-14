<template>
  <input type="checkbox" id="toggle">
  <div class="main_page">
    <!-- POSTS -->
    <!-- <div class="main_page_post">
          <div class="post-box">
            <div class="post-header">
              <div class="btn_box_post">
                <a class="round heart" disabled href="#" title="Понравилось"></a>
                <a class="round open" href="/post/{{post.id}}" title="Открыть полностью">
                  <div class="arrow"></div>
                  <div class="arrow_diff"></div>
                </a>
                <a class="round zakladka" href="add-delete-bookmark" title="В закладки"></a>
              </div>
              <a class="post-author" href="{{post.author.link}}">{{ post.author.name }}</a>
            </div>

            <div class="text-wrap">
              <div class="post-text">{{ post.content }}</div>
            </div>

            {% if post.photo %}
            <img src="{{ post.photo.url }}" class="post-image">
            {% endif %}
          </div>
    </div> -->
    <!-- END POSTS -->

    <!-- Blank 1 -->

    <div class="zero_bookmarks">
      <p class="alarm_posts">У этого пользователя нет постов :c </p>
    </div>
    <!-- Blank 2 -->
    <!-- <div class="zero_bookmarks">
      <p class="alarm_posts">У вас еще нет постов :c </p>
      <a class="btn_add" href="addpost">Написать пост</a>
    </div> -->

  </div>

  <!-- PROFILE CARD -->
  <profile-card :user="user" :userIsMe="userIsMe" />
  <!-- <div class="profile-card-more">
    <p class="user-nickname">Город: {{ profile.city }}</p>
    <p class="user-nickname">Образование: {{ profile.education }}</p>
    <p class="user-nickname">Компания: {{ profile.company }}}</p>
  </div> -->
</template>

<script>
import ProfileCard from '@/components/cards/ProfileCard.vue';


export default {
  components: {
    ProfileCard,
  },
  props: ['id'],
  data() {
    return {
      user: {},
      userIsMe: false,
    }
  },
  async created() {
    let userId = this.$route.params.id;
    await this.$store.dispatch('user/getUser', { id: userId })
      .then(
        response => {
          this.user = response
        }
      )
      .catch(
        reason => {
          this.$router.push(`/profilenotfound`);
          console.log(reason);
        }
      )
    //console.log(this.user)
    this.$store.dispatch('user/isUserSelf', { id: this.user.id }).
      then(response => this.userIsMe = response);
  }
}
</script>

<style>
.btn_profile {
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: 50%;
  font-size: 20px;
  transition: all 0.5s;
  margin: 10px 20%;
  display: inline-block;
  text-align: center;
  transition: all 1s;
}

.btn_profile:hover {
  background-color: #000000;
  border-radius: 12px;
  border: #000000 solid 2px;
  box-shadow: 0px 0px 33px #8270F2;
}

.main_page {
  width: 85%;
  border-radius: 5px;
  margin-top: 7vh;
  margin-bottom: 7vh;
  margin-left: 0;
  transition: all 1s;
}

#toggle {
  appearance: none;
}

#toggle:checked~.profile-card {
  transition: all 1s;
  width: 35%;
}

#toggle:checked~.main_page {
  transition: all 1s;
  width: 70%;
}

.zero_bookmarks {
  background-color: black;
  width: 200px;
  margin: 0 auto;
  display: flex;
  justify-content: center;
  align-items: center;
  flex-wrap: wrap;
  border-radius: 12px;
  padding: 20px;
  box-shadow: 0px 0px 25px #8270F2;

}

.alarm_posts {
  color: white;
}

.btn_posts {
  color: white;
}

.btn_add {
  background-color: #000000;
  border-radius: 12px;
  border: #8270F2 solid 2px;
  padding: 15px;
  color: #8270F2;
  width: 100%;
  font-size: 20px;
  transition: all 0.7s;
  cursor: pointer;
  font-weight: bold;
  text-align: center;
}

.btn_add:hover {
  background: linear-gradient(to top left, #9f49ff, #19087d);
  border-radius: 12px;
  color: white;
  font-weight: bold;
}

#toggle:checked~.profile-card>.user-nickname {
  transition: all 1s;
  width: 30%;
}

#toggle:checked~.profile-card>.user-info {
  transition: all 1s;
  width: 35%;
  right: 0;
  top: 55%;
  position: absolute;
}

#toggle:checked~.profile-card>.profile-pic {
  width: 30%;
  margin: 0 35%;
  border-radius: 100%;
  box-shadow: 0px 0px 30px #8270f2;
  transition: all 1s;
}

.hiddenunckecked {
  overflow: hidden;
  margin: 0 15%;
  padding: 0;
  font-size: 0;
  transition: all 1s;
}

.unhidden {
  transition: all 1s;
  overflow: hidden;
}

#toggle:checked~.profile-card .hiddenunckecked {
  width: 70%;
  margin: 10px 15%;
  padding: 15px 0;
  font-size: 100%;
}

#toggle:checked~.profile-card .user-info {
  height: 85%;
}

#toggle:checked~.profile-card .top {
  margin-bottom: 5px;
}

#toggle:checked~.profile-card .bottom {
  margin-top: 5px;
}


#toggle:checked~.profile-card .unhidden {
  height: 0;
  margin: 0 15%;
  padding: 0;
  font-size: 0;
}

.left {
  width: 100%;
  transition: all 1s;
}

.right {
  overflow: hidden;
  width: 0%;
  transition: all 1s;
}

#toggle:checked~.profile-card .left,
#toggle:checked~.profile-card .right {
  width: 50%;
}

.row {
  display: flex;
}</style>