using System;
using NUnit.Framework;

[TestFixture]
public class ProgramTests
{
    private const string aiSvcKey = "invalid-key";
    private const string aiSvcEndpoint = "invalid-endpoint";

    [Test]
    public void GetLanguage_WithNullText_ReturnsEmptyString()
    {
        // Arrange
        string input = null;

        // Act
        string result = Program.GetLanguage(input);

        // Assert
        Assert.IsEmpty(result);
    }

    [Test]
    public void GetLanguage_WithEmptyText_ReturnsEmptyString()
    {
        // Arrange
        string input = "";

        // Act
        string result = Program.GetLanguage(input);

        // Assert
        Assert.IsEmpty(result);
    }

    [Test]
    public void GetLanguage_WithInvalidApiKey_ThrowsException()
    {
        // Arrange
        string input = "Hello World";

        // Act & Assert
        Assert.Throws<ArgumentException>(() => Program.GetLanguage(input));
    }
}