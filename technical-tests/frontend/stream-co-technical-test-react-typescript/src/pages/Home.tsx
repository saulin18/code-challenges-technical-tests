
import '../App.css'
import Main from '../components/ui/home/Main'
import PopularBanner from '../components/ui/home/PopularTitles'

function Home() {
  return (
    <>
      <PopularBanner>
        Popular Titles
      </PopularBanner>
      <Main />
    </>
  )
}

export default Home
