namespace Currency.Converter;

public static class CurrencyConversion
{
    public static async Task<IResult> Handle(
        string currencyCode,
        decimal amount,
        CurrencyApiClient currencyClient)
    {
        // Validate currency code format (3 uppercase letters)
        if (string.IsNullOrWhiteSpace(currencyCode) ||
            currencyCode.Length != 3 ||
            !currencyCode.All(char.IsLetter))
        {
            return Results.BadRequest(
                new { error = "Currency code must be a 3-letter uppercase code (e.g., EUR, GBP)" });
        }

        // Validate amount (must be positive)
        if (amount < 0)
        {
            return Results.BadRequest(new { error = "Amount must be a positive number" });
        }

        var rate = await currencyClient.GetExchangeRateAsync(currencyCode);

        if (rate == null)
        {
            return Results.NotFound(
                new { error = $"Exchange rate for {currencyCode} not found or API error occurred" });
        }

        var convertedAmount = amount * rate.Value;

        return Results.Ok(new ExchangeRateResponse(
            Currency: currencyCode,
            BaseCurrency: "USD",
            Rate: rate.Value,
            Amount: amount,
            ConvertedAmount: convertedAmount
        ));
    }
}
