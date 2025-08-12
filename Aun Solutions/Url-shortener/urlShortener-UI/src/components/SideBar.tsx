import { useEffect, useState } from "react";
import Detail from "./Detail";





interface openModalProps{
item:any
}


const SideBar=()=>{
    const[list,setList]=useState([])
    const[isOpen,setOpen]=useState(false)
    const [obj, setObj] = useState(Object) 

    useEffect(() => {
    const handleList = async () => {
    try {
      const response = await fetch('http://127.0.0.1:8000/list/', {
        method: 'GET',
        headers: {
          'Content-Type': 'application/json',
        },
      });
      const data = await response.json();
      setList(data.records)
      return data
    } catch (error) {
      console.error('Error finding list:', error);
    }
  };

  handleList();
  
    }, [])
  

    const openModal=({item}:openModalProps)=>{
      setObj(item)
      setOpen(true)
    }

    
  

    return(

        <ul className=" min-h-screen bg-[#273F4F] flex gap-2 flex-col text-white  px-4 py-4 text-sm">
        {list.map((item:any) => {
          return (
            
          <li onClick={()=>{
            openModal({item}) 
          }} className="bg-[#4F8CAA] rounded-lg cursor-pointer px-2 py-2 " key={item.id}>
            <p>{item.short_url}</p> 
          </li>
          
          )
      })}
          <Detail 
          isOpen={isOpen}
          setOpen = {setOpen}
          long = {obj. orignal_url}
          short = {`http://127.0.0.1:8000/${obj.short_url}`}
          clicks = {obj.clicks}
          />
          
        </ul>
    );


}
export default SideBar;