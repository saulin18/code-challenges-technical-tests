import type { MoviesSeriesRepositoryInterface } from "./repository-interface";
import type { Response } from "./domain";
import sampleData from "../../data/sample.json";
import { SortByOptions } from "./repository-interface";
import { isMovie, isSeries } from "./domain";



export function moviesSeriesRepository(): MoviesSeriesRepositoryInterface {

    const getMovies = async (limit: number, releaseYear: number, sortBy: SortByOptions): Promise<Response> => {

        const response = sampleData;
        return {
            entries: response.entries.filter(entry => isMovie(entry) && entry.releaseYear >=releaseYear).sort((a, b) => a[sortBy].localeCompare(b[sortBy])).slice(0, limit)
        }
    }

        const getSeries = async (limit: number, releaseYear: number, sortBy: SortByOptions): Promise<Response> => {
        const response = sampleData;
        return {
            entries: response.entries.filter(entry => isSeries(entry) && entry.releaseYear >= releaseYear).sort((a, b) => a[sortBy].localeCompare(b[sortBy])).slice(0, limit)
        }
    }

    return {
        getMovies,
        getSeries
    }
}    