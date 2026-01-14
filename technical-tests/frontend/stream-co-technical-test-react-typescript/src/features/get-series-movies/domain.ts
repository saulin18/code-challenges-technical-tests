export interface Entry {
    title: string
    description: string
    programType: string
    images: {
        "Poster Art": {
            url: string
            width: number
            height: number
        }
    }
    releaseYear: number
}

const programTypeOfMovies = "movie" as const
const programTypeOfSeries = "series" as const

export interface Response {
    entries: Entry[]
}


export const isSeries = (entry: Entry): boolean => {
    return entry.programType === programTypeOfSeries
}

export const isMovie = (entry: Entry): boolean => {
    return entry.programType === programTypeOfMovies
}