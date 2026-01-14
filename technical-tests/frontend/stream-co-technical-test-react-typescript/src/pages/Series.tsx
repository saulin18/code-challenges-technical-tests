import SeriesList from '../components/ui/SeriesList'
import PopularBanner from '../components/ui/home/PopularTitles'

function Series() {
  return (
    <section className='series-container'>
            <PopularBanner>
            Popular Series
        </PopularBanner>
        <SeriesList />
    </section>
  )
}

export default Series