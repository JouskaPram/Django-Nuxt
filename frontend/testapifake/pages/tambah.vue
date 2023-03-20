<template>
    <div>
        <ul v-for="d in datas " :key="d.id">
            <li>{{ d.id }}</li>
            <li>{{ d.id }}</li>
            <li>{{ d.kategori }}</li>
            <li><button @click="deleteData(d)">Delete</button></li>
            <NuxtLink :to="`/`+d.id">ubah</NuxtLink>
            
        </ul>
        <form @submit.prevent="addCategory">
            <input type="text" v-model="nama">
            <input type="text" v-model="deskripsi">
            <button type="submit">Tambah</button>
        </form>
    </div>
</template>

<script setup>
import axios from 'axios'
const datas = ref([])
const nama = ref()
const deskripsi = ref()
const category = ref() 
const getCategory = async ()=>{
    const res = await axios.get('http://127.0.0.1:8000/api/category/')
    // const data = res.data.sort((a, b) => b.id - a.id ).filter(category => category.kategori === "Makanan")
    datas.value = res.data
    
   
}
const addCategory =  ()=>{
   axios.post('http://127.0.0.1:8000/api/category/',{
    kategori:nama.value,
    deskripsi:deskripsi.value
   })
    getCategory()
}
const deleteData = (d) =>{
    console.log(d.id)
    axios.delete('http://127.0.0.1:8000/api/category/'+d.id+"/")
    getCategory()
}
onMounted(()=>{
    getCategory()
})
</script>
