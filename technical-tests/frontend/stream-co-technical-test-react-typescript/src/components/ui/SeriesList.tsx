
import Card from "./Card"
import type { Entry } from "../../features/get-series-movies/domain"
import './list.css'
import { useMoviesSeries } from "../../hooks/useMoviesSeries"


export default function SeriesList() {

    const {data, isLoading, error} = useMoviesSeries("series")
    if (isLoading) {
        return <div>Loading...</div>
    }

    if (error) {
        return <div>Oops something went wrong</div>
    }


    return (
        <ul className="list-container">
            {data.map((series: Entry) => (
                <li key={series.title}>
            
                <Card >
                    <Card.Content backgroundImage={series.images["Poster Art"].url}>
                        <Card.Title>{series.title}</Card.Title>
                    </Card.Content>
                </Card>
                </li>
            ))}
            </ul>
    )
}