using NUnit.Framework;
using System;

[TestFixture]
public class ProgramTests
{
    private const string aiSvcKey = "your_ai_svc_key";
    private const string aiSvcEndpoint = "your_ai_svc_endpoint";

    [Test]
    public void GetLanguage_ReturnsCorrectLanguage()
    {
        // Arrange
        string inputText = "Hello, world!";
        string expectedLanguage = "English";

        // Act
        string result = Program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual(expectedLanguage, result);
    }

    [Test]
    public void GetLanguage_ReturnsFrenchLanguage()
    {
        // Arrange
        string inputText = "Bonjour le monde!";
        string expectedLanguage = "French";

        // Act
        string result = Program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual(expectedLanguage, result);
    }

    [Test]
    public void GetLanguage_ReturnsSpanishLanguage()
    {
        // Arrange
        string inputText = "Hola el mundo!";
        string expectedLanguage = "Spanish";

        // Act
        string result = Program.GetLanguage(inputText);

        // Assert
        Assert.AreEqual(expectedLanguage, result);
    }
}