import type { Response } from "./domain"


export const SortByOptions = {
    TITLE: "title",
} as const

export type SortByOptions = (typeof SortByOptions)[keyof typeof SortByOptions]

export interface MoviesSeriesRepositoryInterface {

    getMovies(limit: number, releaseYear: number, sortBy: SortByOptions): Promise<Response>
    getSeries(limit: number, releaseYear: number, sortBy: SortByOptions): Promise<Response>

}
