import { useState, useEffect } from "react"
import type { Entry } from "../features/get-series-movies/domain"
import { SortByOptions } from "../features/get-series-movies/repository-interface"
import { moviesSeriesRepository } from "../features/get-series-movies/series-repository-impl"

type MoviesSeriesType = "movies" | "series"

export function useMoviesSeries(type: MoviesSeriesType) {

    const [data, setData] = useState<Entry[]>([])
    const [isLoading, setIsLoading] = useState(true)
    const [error, setError] = useState<string | null>(null)

    useEffect(() => {

        const getMovies = async () => {
            try {
                const response = await moviesSeriesRepository().getMovies(21, 2010, SortByOptions.TITLE)
                setData(response.entries)
                setTimeout(() => {
                    setIsLoading(false)
                }, 1000)
            } catch (error) {
                setError(error as string)
            }
        }

        const getSeries = async () => {
            try {
                const data = await moviesSeriesRepository().getSeries(21, 2010, SortByOptions.TITLE)
                setData(data.entries)
                setTimeout(() => {
                    setIsLoading(false)
                }, 1000)
            } catch (error) {
                setError(error as string)
            }
        }

        if (type === "movies") {
            getMovies()
        } else if (type === "series") {
            getSeries()
        }
    }, [type])

    return { data, isLoading, error }
}   