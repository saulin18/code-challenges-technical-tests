
import Footer from '../components/ui/home/Footer'
import Navbar from '../components/ui/home/Navbar'
import { Outlet } from 'react-router'
function AppLayout() {
  return (
    <main className='app-container'>
      <Navbar />
    
      <Outlet />
      <Footer />
    </main>
  )
}

export default AppLayout