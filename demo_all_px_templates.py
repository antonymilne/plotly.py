"""
Comprehensive demonstration of trace-specific color sequences for ALL Plotly Express charts.

This script systematically goes through every px function, creates templates with trace-specific
colors, and shows side-by-side comparisons with and without templates in a single HTML file.
"""

import plotly.graph_objects as go
import plotly.express as px
import pandas as pd
import numpy as np

# ============================================================================
# Configuration: Map of all px functions to their constructors and trace types
# ============================================================================
PX_FUNCTIONS = {
    # 2D Cartesian plots
    "scatter": (px.scatter, go.Scatter, "scatter"),
    "line": (px.line, go.Scatter, "scatter"),  # Uses Scatter with mode='lines'
    "area": (px.area, go.Scatter, "scatter"),   # Uses Scatter
    "bar": (px.bar, go.Bar, "bar"),
    "timeline": (px.timeline, "timeline", "bar"),  # Special case: maps to bar
    "histogram": (px.histogram, go.Histogram, "histogram"),
    "ecdf": (px.ecdf, go.Scatter, "scatter"),   # Uses Scatter
    "violin": (px.violin, go.Violin, "violin"),
    "box": (px.box, go.Box, "box"),
    "strip": (px.strip, go.Box, "box"),  # Uses Box
    
    # 3D plots
    "scatter_3d": (px.scatter_3d, go.Scatter3d, "scatter3d"),
    "line_3d": (px.line_3d, go.Scatter3d, "scatter3d"),
    
    # Ternary plots
    "scatter_ternary": (px.scatter_ternary, go.Scatterternary, "scatterternary"),
    "line_ternary": (px.line_ternary, go.Scatterternary, "scatterternary"),
    
    # Polar plots
    "scatter_polar": (px.scatter_polar, go.Scatterpolar, "scatterpolar"),
    "line_polar": (px.line_polar, go.Scatterpolar, "scatterpolar"),
    "bar_polar": (px.bar_polar, go.Barpolar, "barpolar"),
    
    # Geographic plots
    "scatter_geo": (px.scatter_geo, go.Scattergeo, "scattergeo"),
    "line_geo": (px.line_geo, go.Scattergeo, "scattergeo"),
    "choropleth": (px.choropleth, go.Choropleth, "choropleth"),
    
    # Map plots
    "scatter_map": (px.scatter_map, go.Scattermap, "scattermap"),
    "line_map": (px.line_map, go.Scattermap, "scattermap"),
    "choropleth_map": (px.choropleth_map, go.Choroplethmap, "choroplethmap"),
    "density_map": (px.density_map, go.Densitymap, "densitymap"),
    
    # Mapbox plots (deprecated but still exist)
    "scatter_mapbox": (px.scatter_mapbox, go.Scattermapbox, "scattermapbox"),
    "line_mapbox": (px.line_mapbox, go.Scattermapbox, "scattermapbox"),
    "choropleth_mapbox": (px.choropleth_mapbox, go.Choroplethmapbox, "choroplethmapbox"),
    "density_mapbox": (px.density_mapbox, go.Densitymapbox, "densitymapbox"),
    
    # Special plots
    "scatter_matrix": (px.scatter_matrix, go.Splom, "splom"),
    "parallel_coordinates": (px.parallel_coordinates, go.Parcoords, "parcoords"),
    "parallel_categories": (px.parallel_categories, go.Parcats, "parcats"),
    
    # Statistical plots
    "density_contour": (px.density_contour, go.Histogram2dContour, "histogram2dcontour"),
    "density_heatmap": (px.density_heatmap, go.Histogram2d, "histogram2d"),
    
    # Hierarchical plots
    "pie": (px.pie, go.Pie, "pie"),
    "sunburst": (px.sunburst, go.Sunburst, "sunburst"),
    "treemap": (px.treemap, go.Treemap, "treemap"),
    "icicle": (px.icicle, go.Icicle, "icicle"),
    "funnel": (px.funnel, go.Funnel, "funnel"),
    "funnel_area": (px.funnel_area, go.Funnelarea, "funnelarea"),
    
    # Image
    "imshow": (px.imshow, go.Image, "image"),
}


# ============================================================================
# Template Creation
# ============================================================================

def create_comprehensive_template():
    """Create a template with marker colors for all trace types.
    
    Merges with default template so we get all default styling plus custom marker colors.
    Uses very distinct colors that are obviously different from Plotly defaults:
    - Plotly defaults: blue, red, teal
    - Template uses: purple, lime, magenta (very distinct color families)
    """
    import plotly.io as pio
    
    # Get default template
    default_template = pio.templates["plotly"]
    
    # Create custom template with only marker colors
    custom_template = go.layout.Template()
    
    # Use the same very distinct colors for ALL trace types
    # These are drastically different from Plotly defaults (blue, red, teal)
    # Using purple, lime, magenta - completely different color families, very distinct from each other
    template_colors = ["purple", "lime", "magenta"]  # Very distinct from Plotly defaults and each other
    
    # Map trace type names to constructors
    trace_constructors = {
        "scatter": go.Scatter,
        "bar": go.Bar,
        "histogram": go.Histogram,
        "box": go.Box,
        "violin": go.Violin,
        "scatter3d": go.Scatter3d,
        "scatterternary": go.Scatterternary,
        "scatterpolar": go.Scatterpolar,
        "barpolar": go.Barpolar,
        "scattergeo": go.Scattergeo,
        "scattermap": go.Scattermap,
        "funnel": go.Funnel,
        "splom": go.Splom,
    }
    
    # Create template data for each trace type - ONLY setting marker.color
    for trace_type, constructor in trace_constructors.items():
        trace_list = []
        for color in template_colors:
            # Only set marker.color, nothing else
            trace_list.append(constructor(marker=dict(color=color)))
        setattr(custom_template.data, trace_type, trace_list)
    
    # Merge default template with custom template using pio.templates.merge_templates
    merged_template = pio.templates.merge_templates(default_template, custom_template)
    
    return merged_template


# ============================================================================
# Helper Functions
# ============================================================================

def test_trace_supports_marker_color(constructor):
    """Test if a trace type supports marker.color."""
    try:
        if constructor == "timeline":
            # Timeline is special, test with Bar
            trace = go.Bar(marker=dict(color="red"))
        elif isinstance(constructor, type):
            trace = constructor(marker=dict(color="red"))
        else:
            return False
        return hasattr(trace, "marker") and hasattr(trace.marker, "color")
    except Exception:
        return False


def get_constructor_name(trace_type):
    """Get the constructor name for a trace type (for code display)."""
    constructor_map = {
        "scatter": "Scatter",
        "bar": "Bar", 
        "histogram": "Histogram",
        "box": "Box",
        "violin": "Violin",
        "scatter3d": "Scatter3d",
        "scatterternary": "Scatterternary",
        "scatterpolar": "Scatterpolar",
        "barpolar": "Barpolar",
        "scattergeo": "Scattergeo",
        "scattermap": "Scattermap",
        "funnel": "Funnel",
        "splom": "Splom",
    }
    return constructor_map.get(trace_type, trace_type.capitalize())


# ============================================================================
# Plot Data Configuration
# ============================================================================

def get_plot_args(px_name, px_fn):
    """Get appropriate arguments for each px function."""
    tips = px.data.tips()
    iris = px.data.iris()
    gapminder = px.data.gapminder().query("year == 2007")
    df_line = px.data.gapminder().query("country in ['Canada', 'Botswana', 'Brazil']")
    wind = px.data.wind()
    election = px.data.election()
    
    args_map = {
        # 2D Cartesian
        "scatter": {"data_frame": iris, "x": "sepal_width", "y": "sepal_length", "color": "species"},
        "line": {"data_frame": df_line, "x": "year", "y": "lifeExp", "color": "country"},
        "area": {"data_frame": df_line, "x": "year", "y": "lifeExp", "color": "country"},
        "bar": {"data_frame": tips, "x": "day", "y": "total_bill", "color": "sex"},
        "timeline": {
            "data_frame": pd.DataFrame([
                dict(Task="Job A", Start='2009-01-01', Finish='2009-02-28', Resource="Alex"),
                dict(Task="Job B", Start='2009-03-05', Finish='2009-04-15', Resource="Alex"),
                dict(Task="Job C", Start='2009-02-20', Finish='2009-05-30', Resource="Max")
            ]),
            "x_start": "Start",
            "x_end": "Finish",
            "y": "Resource",
            "color": "Resource"
        },
        "histogram": {"data_frame": tips, "x": "total_bill", "color": "sex"},
        "ecdf": {"data_frame": tips, "x": "total_bill", "color": "sex"},
        "violin": {"data_frame": tips, "x": "day", "y": "total_bill", "color": "sex"},
        "box": {"data_frame": tips, "x": "day", "y": "total_bill", "color": "sex"},
        "strip": {"data_frame": tips, "x": "day", "y": "total_bill", "color": "sex"},
        
        # 3D
        "scatter_3d": {"data_frame": iris, "x": "sepal_length", "y": "sepal_width", "z": "petal_length", "color": "species"},
        "line_3d": {"data_frame": iris, "x": "sepal_length", "y": "sepal_width", "z": "petal_length", "color": "species"},
        
        # Ternary - use election data as per documentation
        "scatter_ternary": {"data_frame": election, "a": "Joly", "b": "Coderre", "c": "Bergeron", "color": "winner"},
        "line_ternary": {"data_frame": election, "a": "Joly", "b": "Coderre", "c": "Bergeron", "color": "winner"},
        
        # Polar - use wind data as per documentation
        "scatter_polar": {"data_frame": wind, "r": "frequency", "theta": "direction", "color": "strength"},
        "line_polar": {"data_frame": wind, "r": "frequency", "theta": "direction", "color": "strength", "line_close": True},
        "bar_polar": {"data_frame": wind, "r": "frequency", "theta": "direction", "color": "strength"},
        
        # Geographic - skip these as they need special data setup
        "scatter_geo": None,  # Needs lat/lon data
        "line_geo": None,  # Needs lat/lon data
        "choropleth": {"data_frame": gapminder, "locations": "iso_alpha", "color": "lifeExp", "hover_name": "country"},
        
        # Map - skip these as they need special data setup
        "scatter_map": None,  # Needs lat/lon data
        "line_map": None,  # Needs lat/lon data
        "choropleth_map": {"data_frame": gapminder, "geojson": None, "locations": "iso_alpha", "color": "lifeExp"},
        "density_map": None,  # Needs lat/lon data
        
        # Mapbox (deprecated) - skip these as they need special data setup
        "scatter_mapbox": None,  # Needs lat/lon data
        "line_mapbox": None,  # Needs lat/lon data
        "choropleth_mapbox": {"data_frame": gapminder, "geojson": None, "locations": "iso_alpha", "color": "lifeExp"},
        "density_mapbox": None,  # Needs lat/lon data
        
        # Special
        "scatter_matrix": {"data_frame": iris, "dimensions": ["sepal_width", "sepal_length", "petal_width"], "color": "species"},
        "parallel_coordinates": {"data_frame": iris, "dimensions": ["sepal_width", "sepal_length", "petal_width"], "color": "species"},
        "parallel_categories": {"data_frame": tips.head(20), "dimensions": ["sex", "smoker", "day"], "color": "time"},
        
        # Statistical
        "density_contour": {"data_frame": tips, "x": "total_bill", "y": "tip", "color": "sex"},
        "density_heatmap": {"data_frame": tips, "x": "total_bill", "y": "tip"},
        
        # Hierarchical
        "pie": {"data_frame": tips, "names": "day", "values": "total_bill"},
        "sunburst": {
            "data_frame": tips,
            "path": [px.Constant("all"), 'sex', 'day', 'time'],
            "values": "total_bill",
            "color": "day"
        },
        "treemap": {
            "data_frame": tips,
            "path": [px.Constant("all"), 'sex', 'day', 'time'],
            "values": "total_bill",
            "color": "day"
        },
        "icicle": {
            "data_frame": tips,
            "path": [px.Constant("all"), 'sex', 'day', 'time'],
            "values": "total_bill",
            "color": "day"
        },
        "funnel": {
            "data_frame": pd.concat([
                pd.DataFrame(dict(number=[39, 27.4, 20.6, 11, 3], stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"], office=['Montreal']*5)),
                pd.DataFrame(dict(number=[52, 36, 18, 14, 5], stage=["Website visit", "Downloads", "Potential customers", "Requested price", "invoice sent"], office=['Toronto']*5))
            ], axis=0),
            "x": "number",
            "y": "stage",
            "color": "office"
        },
        "funnel_area": {
            "names": ["The 1st", "The 2nd", "The 3rd", "The 4th", "The 5th"],
            "values": [5, 4, 3, 2, 1]
        },
        
        # Image
        "imshow": {"img": np.random.rand(10, 10)},
    }
    
    return args_map.get(px_name, {})


# ============================================================================
# Validation Functions
# ============================================================================

def can_use_discrete_colors(px_name, px_fn, constructor, trace_type):
    """Check if a px function can use discrete colors."""
    # Functions that don't support discrete colors
    no_discrete = {
        "density_heatmap",  # Only continuous
        "density_map",  # Only continuous
        "density_mapbox",  # Only continuous
        "choropleth",  # Only continuous
        "choropleth_map",  # Only continuous
        "choropleth_mapbox",  # Only continuous
        "imshow",  # No color parameter
        "parallel_coordinates",  # Doesn't support discrete colors
        "parallel_categories",  # Doesn't support discrete colors
    }
    
    if px_name in no_discrete:
        return False, "Does not support discrete colors"
    
    # Check if trace type supports marker.color
    if not test_trace_supports_marker_color(constructor):
        return False, "Trace type does not have marker.color attribute"
    
    return True, None


# ============================================================================
# Plot Generation
# ============================================================================

def create_plot_comparison(px_name, px_fn, constructor, trace_type, template):
    """Create a comparison plot for a px function."""
    args = get_plot_args(px_name, px_fn)
    
    if args is None:
        return None, f"No test data configured for {px_name}"
    if not args:
        return None, f"Missing required arguments for {px_name}"
    
    try:
        # Create plot without template
        fig_no_template = px_fn(**args)
        
        # Create plot with template
        args_with_template = args.copy()
        args_with_template["template"] = template
        fig_with_template = px_fn(**args_with_template)
        
        return (fig_no_template, fig_with_template), None
    except Exception as e:
        return None, str(e)


# ============================================================================
# HTML Generation
# ============================================================================

def generate_template_code_display(trace_type):
    """Generate the template code string for display in HTML."""
    template_colors = ["purple", "lime", "magenta"]
    constructor_name = get_constructor_name(trace_type)
    code = f'template.data.{trace_type} = [\n'
    for color in template_colors:
        code += f'    go.{constructor_name}(marker=dict(color="{color}")),\n'
    code += ']'
    return code


def generate_html_content(works_with_template):
    """Generate the complete HTML content with embedded images."""
    html_content = """
<!DOCTYPE html>
<html>
<head>
    <title>Plotly Express Template Color Demonstration</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 1400px;
            margin: 0 auto;
            padding: 20px;
            background-color: #f5f5f5;
        }
        h1 {
            color: #333;
            text-align: center;
        }
        .plot-section {
            background-color: white;
            padding: 20px;
            margin-bottom: 20px;
            border-radius: 5px;
        }
        .plot-container {
            display: flex;
            gap: 20px;
            margin-top: 15px;
        }
        .plot-box {
            flex: 1;
            text-align: center;
        }
        .plot-box h3 {
            margin-top: 0;
            color: #666;
        }
        img {
            max-width: 100%;
            height: auto;
        }
        pre {
            margin-top: 15px;
            padding: 10px;
            background-color: #f9f9f9;
            border-radius: 4px;
            font-size: 12px;
            overflow-x: auto;
        }
        code {
            font-family: 'Courier New', monospace;
        }
    </style>
</head>
<body>
    <h1>Plotly Express Template Color Demonstration</h1>
"""
    
    import base64
    from io import BytesIO
    
    for px_name, (fig_no, fig_with), trace_type in works_with_template:
        try:
            # Generate PNG images as base64-encoded data URIs
            img_buffer_no = BytesIO()
            fig_no.write_image(img_buffer_no, format='png', width=700, height=500, scale=2)
            img_buffer_no.seek(0)
            img_base64_no = base64.b64encode(img_buffer_no.read()).decode('utf-8')
            
            img_buffer_with = BytesIO()
            fig_with.write_image(img_buffer_with, format='png', width=700, height=500, scale=2)
            img_buffer_with.seek(0)
            img_base64_with = base64.b64encode(img_buffer_with.read()).decode('utf-8')
            
            print(f"    Generated embedded images for {px_name}")
            
            # Generate template code for display
            template_code = generate_template_code_display(trace_type)
            
            # Add plot section to HTML
            html_content += f"""
        <div class="plot-section">
            <h3>{px_name.replace('_', ' ').title()}</h3>
            <div class="plot-container">
                <div class="plot-box">
                    <h3>Without Template</h3>
                    <img src="data:image/png;base64,{img_base64_no}" alt="{px_name} without template">
                </div>
                <div class="plot-box">
                    <h3>With Template</h3>
                    <img src="data:image/png;base64,{img_base64_with}" alt="{px_name} with template">
                    <pre style="margin-top: 15px; padding: 10px; background-color: #f9f9f9; border-radius: 4px; font-size: 12px; overflow-x: auto; text-align: left;"><code>{template_code}</code></pre>
                </div>
            </div>
        </div>
        """
        except Exception as e:
            print(f"    Warning: Could not generate images for {px_name}: {e}")
    
    html_content += """
    </body>
    </html>
    """
    
    return html_content


# ============================================================================
# Main Function
# ============================================================================

def main():
    """Generate comprehensive demonstration."""
    print("="*80)
    print("Comprehensive Plotly Express Template Color Demonstration")
    print("="*80)
    
    template = create_comprehensive_template()
    
    # Categorize all px functions - only keep working ones
    works_with_template = []
    
    print("\nAnalyzing all Plotly Express functions...")
    print("-" * 80)
    
    for px_name, (px_fn, constructor, trace_type) in PX_FUNCTIONS.items():
        can_use, reason = can_use_discrete_colors(px_name, px_fn, constructor, trace_type)
        
        if can_use:
            result, error = create_plot_comparison(px_name, px_fn, constructor, trace_type, template)
            if result:
                works_with_template.append((px_name, result, trace_type))
                print(f"✓ {px_name:30} - Works (uses template.data.{trace_type})")
    
    print("\n" + "="*80)
    print("Creating HTML file...")
    
    # Generate HTML content
    html_content = generate_html_content(works_with_template)
    
    # Write to file
    with open("all_px_template_demo.html", "w") as f:
        f.write(html_content)
    
    print(f"  ✓ Created all_px_template_demo.html")
    print(f"\nGenerated {len(works_with_template)} working comparisons")
    
    print("\n" + "="*80)
    print("Complete! Open all_px_template_demo.html in a browser to see all comparisons.")
    print("="*80)


if __name__ == "__main__":
    main()

