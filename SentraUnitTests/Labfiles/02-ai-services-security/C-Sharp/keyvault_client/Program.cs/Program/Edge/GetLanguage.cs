using Azure.AI.TextAnalytics;
using Azure.Core.TestFramework;
using NUnit.Framework;

public class ProgramTests : RecordedTestBase<ProgramFixture>
{
    [Test]
    public void GetLanguage_WithEmptyText_ReturnsUnknown()
    {
        string result = Program.GetLanguage("");
        Assert.AreEqual("Unknown", result);
    }

    [Test]
    public void GetLanguage_WithSingleWord_ReturnsCorrectLanguage()
    {
        string result = Program.GetLanguage("Hello");
        Assert.AreEqual("English", result);
    }

    [Test]
    public void GetLanguage_WithMultipleLanguages_ReturnsCorrectLanguage()
    {
        string result = Program.GetLanguage("Bonjour le monde");
        Assert.AreEqual("French", result);
    }
}

internal class ProgramFixture : RecordedTestBase<ProgramFixture>
{
    public string aiSvcKey { get; set; } = "your-key-here";
    public string aiSvcEndpoint { get; set; } = "https://your-endpoint-here.cognitiveservices.azure.com/";
}