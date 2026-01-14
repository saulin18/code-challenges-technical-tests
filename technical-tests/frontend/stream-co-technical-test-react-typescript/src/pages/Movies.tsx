import React from 'react'
import MoviesList from '../components/ui/MoviesList'
import PopularBanner from '../components/ui/home/PopularTitles'


function Movies() {
  return (
    <section className='movies-container'>
        <PopularBanner>
            Popular Movies
        </PopularBanner>
        <MoviesList />
    </section>
  )
}

export default Movies