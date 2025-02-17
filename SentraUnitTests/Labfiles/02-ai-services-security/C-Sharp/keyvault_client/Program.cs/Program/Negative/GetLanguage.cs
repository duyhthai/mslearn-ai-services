using System;
using NUnit.Framework;

[TestFixture]
public class ProgramTests
{
    private const string aiSvcKey = "invalid_key";
    private const string aiSvcEndpoint = "https://invalid-endpoint.cognitiveservices.azure.com/";

    [Test]
    public void GetLanguage_InvalidApiKey_ReturnsNull()
    {
        // Arrange
        string text = "Hello world";

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.IsNull(result);
    }

    [Test]
    public void GetLanguage_InvalidEndpoint_ReturnsNull()
    {
        // Arrange
        string text = "Hello world";

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.IsNull(result);
    }

    [Test]
    public void GetLanguage_EmptyText_ReturnsNull()
    {
        // Arrange
        string text = "";

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.IsNull(result);
    }
}