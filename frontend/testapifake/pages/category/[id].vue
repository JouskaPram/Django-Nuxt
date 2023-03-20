<template>
    <div>
        <p>id:{{ datas.id }}</p>
        <p>kategori:{{datas.kategori}}</p>
        <p>deskripsi: {{ datas.deskripsi }}</p>
    <form  method="post" @submit.prevent="updateCategory" >
        <input type="text" required v-model="kategori" placeholder="kategori">
        <textarea  id="" cols="30" rows="10" required v-model="deskripsi" placeholder="deskripsi"></textarea>
        <button type="submit">Ubah</button>
    </form>
    </div>
</template>

<script setup>
import axios from  "axios"
const route = useRoute()
const url = ref("http://127.0.0.1:8000/api/category/")
const kategori = ref()
const deskripsi = ref()
const datas = ref([])
const getCategory = async ()=>{
    const res = await axios.get(url.value+route.params.id+"/")
    
   
    datas.value = res.data
    console.log(datas.value)
}
const updateCategory = async () =>{
     await axios.put(url.value+route.params.id+"/",({
        kategori:kategori.value,
        deskripsi:deskripsi.value
        
    }))
    getCategory()
}
onMounted(()=>{
    getCategory()
})
</script>
