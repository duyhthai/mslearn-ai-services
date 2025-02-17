using NUnit.Framework;
using System;

[TestFixture]
public class ProgramTests
{
    private const string AISvcKey = "your_key_here";
    private const string AISvcEndpoint = "your_endpoint_here";

    [Test]
    public void GetLanguage_WithEnglishText_ReturnsEnglish()
    {
        // Arrange
        string text = "Hello, how are you?";
        var program = new Program();

        // Act
        string result = program.GetLanguage(text);

        // Assert
        Assert.AreEqual("English", result);
    }

    [Test]
    public void GetLanguage_WithSpanishText_ReturnsSpanish()
    {
        // Arrange
        string text = "Hola, ¿cómo estás?";
        var program = new Program();

        // Act
        string result = program.GetLanguage(text);

        // Assert
        Assert.AreEqual("Spanish", result);
    }

    [Test]
    public void GetLanguage_WithFrenchText_ReturnsFrench()
    {
        // Arrange
        string text = "Bonjour, comment allez-vous aujourd'hui ?";
        var program = new Program();

        // Act
        string result = program.GetLanguage(text);

        // Assert
        Assert.AreEqual("French", result);
    }
}