using Microsoft.VisualStudio.TestTools.UnitTesting;
using Azure.AI.TextAnalytics;
using System;

[TestClass]
public class ProgramTests
{
    private const string AISvcKey = "your_key_here";
    private const string AISvcEndpoint = "https://your_endpoint_here.cognitiveservices.azure.com/";

    [TestMethod]
    public void GetLanguage_WithEmptyString_ReturnsUnknown()
    {
        // Arrange
        string inputText = "";
        var program = new Program();

        // Act
        string result = program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual("Unknown", result);
    }

    [TestMethod]
    public void GetLanguage_WithNullString_ReturnsUnknown()
    {
        // Arrange
        string inputText = null;
        var program = new Program();

        // Act
        string result = program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual("Unknown", result);
    }

    [TestMethod]
    public void GetLanguage_WithValidEnglishText_ReturnsEnglish()
    {
        // Arrange
        string inputText = "Hello, how are you?";
        var program = new Program();

        // Act
        string result = program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual("English", result);
    }
}