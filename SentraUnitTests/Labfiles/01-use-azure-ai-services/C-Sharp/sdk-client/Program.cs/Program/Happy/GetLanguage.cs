using Xunit;
using System;

public class ProgramTests
{
    private const string AISvcKey = "your-api-key";
    private const string AISvcEndpoint = "your-api-endpoint";

    [Fact]
    public void GetLanguage_WithEnglishText_ReturnsEnglish()
    {
        // Arrange
        string text = "Hello, how are you?";
        
        // Act
        string result = Program.GetLanguage(text);
        
        // Assert
        Assert.Equal("English", result);
    }

    [Fact]
    public void GetLanguage_WithSpanishText_ReturnsSpanish()
    {
        // Arrange
        string text = "Hola, ¿cómo estás?";
        
        // Act
        string result = Program.GetLanguage(text);
        
        // Assert
        Assert.Equal("Spanish", result);
    }

    [Fact]
    public void GetLanguage_WithFrenchText_ReturnsFrench()
    {
        // Arrange
        string text = "Bonjour, comment allez-vous ?";
        
        // Act
        string result = Program.GetLanguage(text);
        
        // Assert
        Assert.Equal("French", result);
    }
}