using NUnit.Framework;
using System;

[TestFixture]
public class ProgramTests
{
    private const string aiSvcKey = "your_key_here";
    private const string aiSvcEndpoint = "your_endpoint_here";

    [Test]
    public void GetLanguage_WithEmptyText_ReturnsUnknown()
    {
        // Arrange
        string text = "";

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.AreEqual("Unknown", result);
    }

    [Test]
    public void GetLanguage_WithSingleWordEnglish_ReturnsEnglish()
    {
        // Arrange
        string text = "Hello";

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.AreEqual("English", result);
    }

    [Test]
    public void GetLanguage_WithSentenceInSpanish_ReturnsSpanish()
    {
        // Arrange
        string text = "Hola mundo";

        // Act
        string result = Program.GetLanguage(text);

        // Assert
        Assert.AreEqual("Spanish", result);
    }
}