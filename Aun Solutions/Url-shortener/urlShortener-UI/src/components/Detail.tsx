import Modal from 'react-modal';
import  type {FC} from "react";


interface ModalProps{
    isOpen: boolean
    setOpen: React.Dispatch<React.SetStateAction<boolean>>
    short : string
    long : string
    clicks : string
}



const Detail : FC<ModalProps> = ({isOpen, setOpen, short, long, clicks})=>{

    function closeModal(){
      setOpen(false)
    }
return(
    // <div className="h-[100vh] w-[100%] flex item-center justify-center">
    <Modal className="w-[80%] bg-white mx-auto mt-[15rem] px-[3rem]"
    isOpen={isOpen}
    onRequestClose={closeModal}
    > 
    <p>URL : {long}</p>
    <p>Short URL : {short}</p>
    <p>NO. of Clicks : {clicks}</p>
    
    
    </Modal>
    // </div>
)   
}


export default Detail;